(defun list-union (L1 L2) (cond
			   ((null L1) L2)
			   ((null L2) L1)
			   ((member (first L1) L2) (list-union (rest L1) L2))
			   (t (cons (first L1) (list-union (rest L1) L2)))))

(defun list-inters (L1 L2) (cond
			    ((or (null L1) (null L2)) nil)
			    ((member (first L1) L2) (cons (first L1) (list-inters (rest L1) L2)))
			    (t (list-inters (rest L1) L2))))