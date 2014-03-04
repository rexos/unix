(defun list-butlast (L) (cond
			 ((or (null L) (= (length L) 1)) nil)
			 (t (cons (first L) (list-butlast (rest L))))))