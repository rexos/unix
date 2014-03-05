(defun double (x) (* 2 x))

(defun blah-build (L) (cons 'blah L))

(defun selector (L) (rest L))

;; zerop -> (= n 0)
;; example of higher-order function (because it takes a function argument)
(defun repeat (F n x) 
  (if (zerop n) x
    (repeat F (1- n) (funcall F x))))

(repeat (function double) 8 1)
;; alternative way
(repeat #'double 8 1)
(funcall (function double) 4)