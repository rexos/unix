(defun binomial (x y) (if (or (zerop y) (= y x)) 1
			(+ (binomial (1- x) (1- y)) (binomial (1- x) y))))