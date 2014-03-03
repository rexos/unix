(defun fibonacci (n) (if (or (zerop n) (= n 1)) 1 
		      (+ (fibonacci (1- n) (fibonacci (- n 2))))))