(defun list-len (x)
  (if (null x) 0 
    (1+ (list-len (rest x)))))

(defun sumup (L)
  (if (null L) 0
    (+ (first L) (sumup (rest L)))))