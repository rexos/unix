(defun nth-list (n L) (if (null L) nil 
			(if (zerop n) (first L)
			  (nth-list (1- n) (rest L)))))

(defun last-list (L) (if (null L) nil 
		  (if (= (list-length L) 1) (first L) 
		    (last-list (rest L)))))