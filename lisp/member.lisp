;;; memeber recursive implementation

(defun list-member (e L) (cond
			   ((null L) nil)
			   ((equal e (first L)) L)
			   (t (list-member e (rest L)))))