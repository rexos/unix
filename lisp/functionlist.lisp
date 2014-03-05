;; magic
(defun functionlist (F L) 
  (if (null F) L
    (funcall (first F) (functionlist (rest F) L))))

;; test functionlist using also a lambda function
(functionlist (list #'(lambda (x) (* 10 x)) #'fourth) '(10 20 30 40 50))
;; another call
(functionlist (list #'third #'second) '((1 2) (3 4 5) (6)))
;; again
(functionlist (list #'(lambda (x) (- 10 x)) #'length) '(a b c d e f))
;; and again
(functionlist (list #'list #'list) 'blah)