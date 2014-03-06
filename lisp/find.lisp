;;; find-if usage

(defun length-three (L) 
  (find-if #'(lambda (x) (>= (length x) 3)) L))

(defun even-list (L) 
  (find-if #'(lambda (x) (evenp (length x))) L))