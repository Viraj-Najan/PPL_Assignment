(defun findnth (n list)
	(setq c 0)
	(dolist (l list)
		(incf c 1)
		(if (= c n)
			(return 1)
		)
	)
)

(write-line "Enter the list : ")
(defvar a (read-from-string (concatenate 'string "(" (read-line) ")")))
(write a)
(terpri)
(write-line "Enter the value of n: ")
(setq n (read))
(write (findnth n a))
