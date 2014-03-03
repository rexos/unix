(defun triangle (n) (if (= n 1) 1 
		      (+ n (triangle (- n 1)))))