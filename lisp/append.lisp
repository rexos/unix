(defun list-append (H E) (cond
			  ((null H) E)
			  ((null E) H)
			  (t (cons (first H) (list-append (rest H) E)))))