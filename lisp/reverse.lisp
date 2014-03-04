(load "nth.lisp")

(defun list-reverse (L) (cond
			 ((null L) nil)
			 (t (cons (last-list L) (list-reverse (butlast L))))))