;; map implementation
(defun map-list (F L) 
  (if (null L) nil
  (cons (funcall F (first L)) (map-list F (rest L)))))

(map-list #'(lambda (x) (* x x)) '(1 2 3 4))