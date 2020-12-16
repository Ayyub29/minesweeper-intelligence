(deftemplate tile
    (slot x )
    (slot y )
    (slot hidden_neigh)
    (slot flag_neigh)
    (slot value)
)

(deftemplate bomb
    (slot x )
    (slot y )
)

(deftemplate flag
    (slot x )
    (slot y )
)

(deftemplate opened
    (slot x)
    (slot y)
)

(deftemplate decrement_hn
    (slot x)
    (slot y)
)

(deftemplate decrement_fn
    (slot x)
    (slot y)
)

(deftemplate val
    (slot x)
    (slot y)
    (slot v)
)

;;cek bomb
;;;(deffacts initial-states 
;;;    (opened (x 0) (y 0))
;;;    (opened (x 0) (y 2))
;;;    (opened (x 1) (y 0))
;;;    (opened (x 1) (y 1))
;;;    (opened (x 1) (y 2))
;;;    (opened (x 2) (y 0))
;;;    (opened (x 2) (y 1))
;;;
;;;
;;;    (tile (x 0) (y 0) (hidden_neigh 1) (flag_neigh 0) (value 1))
;;;    (tile (x 0) (y 1) (hidden_neigh 0) (flag_neigh 0) (value -1))
;;;    (tile (x 0) (y 2) (hidden_neigh 1) (flag_neigh 0) (value 1))
;;;    (tile (x 1) (y 0) (hidden_neigh 1) (flag_neigh 0) (value 1))
;;;    (tile (x 1) (y 1) (hidden_neigh 1) (flag_neigh 1) (value 2))
;;;    (tile (x 1) (y 2) (hidden_neigh 1) (flag_neigh 1) (value 2))
;;;    (tile (x 2) (y 0) (hidden_neigh 0) (flag_neigh 0) (value 0))
;;;    (tile (x 2) (y 1) (hidden_neigh 0) (flag_neigh 1) (value 1))
;;;    (tile (x 2) (y 2) (hidden_neigh 0) (flag_neigh 0) (value -2))
;;;)

;;cek not bomb
;;;(deffacts initial-states 
;;;    (opened (x 1) (y 0))
;;;    (opened (x 1) (y 1))
;;;    (opened (x 1) (y 2))
;;;    (opened (x 2) (y 0))
;;;    (opened (x 2) (y 1))
;;;
;;;
;;;    (tile (x 0) (y 0) (hidden_neigh 1) (flag_neigh 0) (value -1))
;;;    (tile (x 0) (y 1) (hidden_neigh 2) (flag_neigh 0) (value -1))
;;;    (tile (x 0) (y 2) (hidden_neigh 1) (flag_neigh 0) (value -1))
;;;    (tile (x 1) (y 0) (hidden_neigh 2) (flag_neigh 0) (value 0))
;;;    (tile (x 1) (y 1) (hidden_neigh 3) (flag_neigh 1) (value 1))
;;;    (tile (x 1) (y 2) (hidden_neigh 2) (flag_neigh 1) (value 1))
;;;    (tile (x 2) (y 0) (hidden_neigh 0) (flag_neigh 0) (value 0))
;;;    (tile (x 2) (y 1) (hidden_neigh 0) (flag_neigh 1) (value 1))
;;;    (tile (x 2) (y 2) (hidden_neigh 0) (flag_neigh 0) (value -2))
;;;)

; ;;cek chacha
(deffacts initial-states 
    (opened (x 0) (y 0))
    (val (x 0) (y 0) (v 0))
    (tile (x 0) (y 0) (hidden_neigh 3) (flag_neigh 0) (value -1))
    (val (x 0) (y 1) (v 0))
    (tile (x 0) (y 1) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 0) (y 2) (v 0))
    (tile (x 0) (y 2) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 0) (y 3) (v 0))
    (tile (x 0) (y 3) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 0) (y 4) (v 0))
    (tile (x 0) (y 4) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 1) (y 0) (v 0))
    (tile (x 1) (y 0) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 1) (y 1) (v 0))
    (tile (x 1) (y 1) (hidden_neigh 8) (flag_neigh 0) (value -1))
    (val (x 1) (y 2) (v 0))
    (tile (x 1) (y 2) (hidden_neigh 8) (flag_neigh 0) (value -1))
    (val (x 1) (y 3) (v 1))
    (tile (x 1) (y 3) (hidden_neigh 8) (flag_neigh 0) (value -1))
    (val (x 1) (y 4) (v 1))
    (tile (x 1) (y 4) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 2) (y 0) (v 0))
    (tile (x 2) (y 0) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 2) (y 1) (v 0))
    (tile (x 2) (y 1) (hidden_neigh 8) (flag_neigh 0) (value -1))
    (val (x 2) (y 2) (v 1))
    (tile (x 2) (y 2) (hidden_neigh 8) (flag_neigh 0) (value -1))
    (val (x 2) (y 3) (v 3))
    (tile (x 2) (y 3) (hidden_neigh 8) (flag_neigh 0) (value -1))
    (val (x 2) (y 4) (v 5))
    (tile (x 2) (y 4) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 3) (y 0) (v 0))
    (tile (x 3) (y 0) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 3) (y 1) (v 1))
    (tile (x 3) (y 1) (hidden_neigh 8) (flag_neigh 0) (value -1))
    (val (x 3) (y 2) (v 2))
    (tile (x 3) (y 2) (hidden_neigh 8) (flag_neigh 0) (value -1))
    (val (x 3) (y 3) (v 5))
    (tile (x 3) (y 3) (hidden_neigh 8) (flag_neigh 0) (value -1))
    (val (x 3) (y 4) (v 5))
    (tile (x 3) (y 4) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 4) (y 0) (v 0))
    (tile (x 4) (y 0) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 4) (y 1) (v 1))
    (tile (x 4) (y 1) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 4) (y 2) (v 5))
    (tile (x 4) (y 2) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 4) (y 3) (v 3))
    (tile (x 4) (y 3) (hidden_neigh 5) (flag_neigh 0) (value -1))
    (val (x 4) (y 4) (v 2))
    (tile (x 4) (y 4) (hidden_neigh 3) (flag_neigh 0) (value -1))
    (decrement_fn (x 1) (y 3))
    (decrement_fn (x 1) (y 4))
    (decrement_fn (x 0) (y 4))
    (decrement_fn (x 2) (y 2))
    (decrement_fn (x 3) (y 1))
    (decrement_fn (x 4) (y 1))
    (decrement_fn (x 4) (y 0))
    (decrement_fn (x 3) (y 0))
    (decrement_fn (x 2) (y 0))
    (decrement_fn (x 3) (y 2))
    (decrement_fn (x 2) (y 1))
    (decrement_fn (x 1) (y 0))
    (decrement_fn (x 1) (y 1))
    (decrement_fn (x 2) (y 3))
    (decrement_fn (x 1) (y 2))
    (decrement_fn (x 0) (y 3))
    (decrement_fn (x 0) (y 2))
    (decrement_fn (x 0) (y 1))
)


(defrule startup
    =>
    (printout t crlf "Minesweeper" crlf crlf)
    (printout t " 3x3 " crlf)
)

(defrule openn
    (opened (x ?x) (y ?y))
    (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?v))

    (val (x ?a) (y ?b) (v ?c))
    (test (eq ?a ?x))
    (test (eq ?b ?y))
    =>
    (assert 
        (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?c))
    )
)


(defrule isClear
    (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?v))
    (test (eq ?v ?f))

    ?gg <- (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value ?v1))
    (test (eq ?v1 -1))

    
    (or (and (test (eq ?x ?x1)) (or (test (eq ?y (+ ?y1 1))) (test (eq ?y (+ ?y1 -1))))) 
        (or 
            (and (test (eq ?y ?y1)) (or (test (eq ?x (+ ?x1 1))) (test (eq ?x (+ ?x1 -1))) )) 
            (and (or (test (eq ?x (+ ?x1 1))) (test (eq ?x (+ ?x1 -1))))  (or (test (eq ?y (+ ?y1 1))) (test (eq ?y (+ ?y1 -1)))) ) 
        )
    )

    (val (x ?a) (y ?b) (v ?c))
    (test (eq ?a ?x1))
    (test (eq ?b ?y1))
 
    =>
    (retract ?gg)
    (assert (opened (x ?x1) (y ?y1))
            (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value ?c))
            (decrement_fn (x (+ ?x1 -1)) (y (+ ?y1 -1)) )
            (decrement_fn (x (+ ?x1 -1)) (y ?y1) )
            (decrement_fn (x (+ ?x1 -1)) (y (+ ?y1 1)) )

            (decrement_fn (x ?x1) (y (+ ?y1 -1)) )
            (decrement_fn (x ?x1) (y (+ ?y1 1)) )

            (decrement_fn (x (+ ?x1 1)) (y (+ ?y1 -1)) )
            (decrement_fn (x (+ ?x1 1)) (y ?y1) )
            (decrement_fn (x (+ ?x1 1)) (y (+ ?y1 1)) )
    )
    
    (printout t "isClear:" crlf)
    (printout t  ?x ?y crlf)
    (printout t  ?x1 ?y1 crlf)
    (printout t  crlf)
)

(defrule isBomb
    (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?v))
    (test (eq ?v ?h))

    ?gg <- (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value ?v1))
    (test (eq ?v1 -1))

    (or (and (test (eq ?x ?x1)) (or (test (eq ?y (+ ?y1 1))) (test (eq ?y (+ ?y1 -1))))) 
        (or 
            (and (test (eq ?y ?y1)) (or (test (eq ?x (+ ?x1 1))) (test (eq ?x (+ ?x1 -1))) )) 
            (and (or (test (eq ?x (+ ?x1 1))) (test (eq ?x (+ ?x1 -1))))  (or (test (eq ?y (+ ?y1 1))) (test (eq ?y (+ ?y1 -1)))) ) 
        )
    ) 

    =>

    (retract ?gg)
    (assert (bomb (x ?x1) (y ?y1))
            (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value -2))
            (decrement_hn (x (+ ?x1 -1)) (y (+ ?y1 -1)) )
            (decrement_hn (x (+ ?x1 -1)) (y ?y1) )
            (decrement_hn (x (+ ?x1 -1)) (y (+ ?y1 1)) )

            (decrement_hn (x ?x1) (y (+ ?y1 -1)) )
            (decrement_hn (x ?x1) (y (+ ?y1 1)) )

            (decrement_hn (x (+ ?x1 1)) (y (+ ?y1 -1)) )
            (decrement_hn (x (+ ?x1 1)) (y ?y1) )
            (decrement_hn (x (+ ?x1 1)) (y (+ ?y1 1)) )
    )
    
    (printout t "isBomb:" crlf)
    (printout t  ?x ?y crlf)
    (printout t  ?x1 ?y1 crlf)
    (printout t  crlf)
    
    ;;;(printout t  ?x1 ?y1 crlf)
)

(defrule change_isBomb
    ?hh <- (decrement_hn (x ?x) (y ?y))
    ?gg <- (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?v))
    (test (neq ?h 0))
    =>
    
    (assert 
        (tile (x ?x) (y ?y) (hidden_neigh (+ ?h -1)) (flag_neigh (+ ?f 1)) (value ?v))
    )
    (retract ?gg ?hh)
)

(defrule change_isClear
    ?hh <- (decrement_fn (x ?x) (y ?y))
    ?gg <- (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?v))
    (test (neq ?h 0))
    =>
    (assert 
        (tile (x ?x) (y ?y) (hidden_neigh (+ ?h -1)) (flag_neigh ?f) (value ?v))
    )
    (retract ?gg ?hh)
)

