(defun triangle (n) (if (= n 1) 1 
		      (+ n (triangle (- n 1)))))

(defun fast-triangle (n) 
  (fast-triangle-aux n 1))
(defun fast-triangle-aux (n a) 
  (if (= n 1) a 
    (fast-triangle-aux (1- n) (+ n a))))