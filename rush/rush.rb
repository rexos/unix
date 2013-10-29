#! /usr/bin/env ruby
require 'shellwords'

BUILTINS = {
  'cd' => lambda { |dir| Dir.chdir(dir) },
  'exit' => lambda { |code = 0| exit( code.to_i ) },
  'exec' => lambda { |*command| exec *command },
  'set' => lambda { |args|
  	key, value = args.split( '=' )
	ENV[key] = value
	},
  'del' => lambda { |key| ENV.delete( key ) }
}

def builtin?( prog )
  !BUILTINS[prog].nil?
end

def split_by_pipe( line )
  line.scan( /([^"'|]+)|["']([^"']+)["']/ ).flatten.compact
end

def split_by_greater( command )
  command.scan( /([^"'>]+)|[']([^']+)[']/ ).flatten.compact
end

def execute_program( command, *arguments, plain, plaout )
  fork {
    $stdout.reopen( plaout ) unless plaout == $stdout
    $stdin.reopen( plain ) unless plain == $stdin
    begin
      if command.include? ">"
        command, *arguments = Shellwords.shellsplit( command )
        file_name = command.last
        #to be continued
      else
        exec command, *arguments
      end
    rescue Errno::ENOENT => exce
      puts "#{command} : No such file or directory"
    end
  }
end

loop do
  $stdout.print "[#{Dir.getwd} - rush] ~> "

  line = $stdin.gets.strip
  commands = split_by_pipe( line )

  plain = $stdin
  plaout = $stdout
  pipe = []

  commands.each_with_index do |c, i|
    command, *arguments = Shellwords.shellsplit( c )

    if builtin?( command )
      BUILTINS[command].call( *arguments )
      break
    end
    if i + 1 < commands.size
      pipe = IO.pipe
      plaout = pipe.last
    else
      plaout = $stdout
    end

    execute_program( command, *arguments, plain, plaout )

    plaout.close unless plaout == $stdout
    plain.close unless plain == $stdin
    plain = pipe.first
  end
  Process.waitall
end
