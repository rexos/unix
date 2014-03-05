(defun nempty (L) 
  ;; returns the leftmost non-empty value of a list
  (if (null L) nil
    (if (null (first L)) 
	(nempty (rest L))
      (first L))))