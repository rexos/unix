(defun remove-where (P L) 
  (if (null L) nil
    (if (not (funcall P (first L))) 
	(cons (first L) (remove-where P (rest L)))
      (remove-where P (rest L)))))

;; call to remove elements with size < 3
(remove-where #'(lambda (x) (< (length x) 3)) '((1) (2 3 4) (3)))