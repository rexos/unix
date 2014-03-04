(defun list-len (x)
  (if (null x) 0 
    (1+ (list-len (rest x)))))

;; allows tail recursion
(defun fast-length (L)
  (fast-length-aux L 0))
(defun fast-length-aux (L n) 
  (if (null L) n 
    (fast-length-aux (rest L) (1+ n))))

(defun sumup (L)
  (if (null L) 0
    (+ (first L) (sumup (rest L)))))