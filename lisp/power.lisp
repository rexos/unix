(defun power (x y) (if (= y 0) 1 
		     (* x (power x (- y 1)))))

;; allows tail recursion

(defun fast-power (x y) 
  (fast-power-aux x y 1))
(defun fast-power-aux (x y n) 
  (if (= y 0) n 
    (fast-power-aux x (1- y) (* x n))))