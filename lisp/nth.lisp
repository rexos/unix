;;#! $(which clisp)

(defun nth-list (n L) (if (null L) nil 
			(if (zerop n) (first L)
			  (nth-list (1- n) (rest L)))))

(defun last-list (L) (if (null L) nil 
		  (if (= (list-length L) 1) (first L) 
		    (last-list (rest L)))))

;; using COND instead of IF

(defun last-cond (L) (cond
		      ((null L) nil)
		      ((= (list-length L) 1) (first L))
		      (t (last-cond (rest L)))))

(princ (last-cond '(4 3 f a 4 6 1 6 7 8 12)))