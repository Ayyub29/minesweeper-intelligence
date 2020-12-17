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

(deftemplate decrement_hn_all
    (slot x)
    (slot y)
)

(deftemplate decrement_fn_all
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

((deffacts initial-states
    (opened (x 0) (y 1))
    (opened (x 0) (y 2))
    (opened (x 0) (y 3))
    (opened (x 0) (y 4))
    (opened (x 1) (y 0))
    (opened (x 1) (y 1))
    (opened (x 1) (y 2))
    (opened (x 1) (y 3))
    (opened (x 1) (y 4))
    (opened (x 2) (y 0))
    (opened (x 2) (y 1))
    (opened (x 2) (y 2))
    (opened (x 2) (y 3))
    (opened (x 3) (y 0))
    (opened (x 3) (y 1))
    (opened (x 3) (y 2))
    (opened (x 3) (y 3))
    (opened (x 4) (y 0))
    (opened (x 4) (y 1))
    (opened (x 4) (y 2))
    (tile (x 0) (y 0) (hidden_neigh 0) (flag_neigh 0) (value -1))
    (tile (x 0) (y 1) (hidden_neigh 1) (flag_neigh 0) (value 1))
    (tile (x 0) (y 2) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 0) (y 3) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 0) (y 4) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 1) (y 0) (hidden_neigh 1) (flag_neigh 0) (value 1))
    (tile (x 1) (y 1) (hidden_neigh 1) (flag_neigh 0) (value 1))
    (tile (x 1) (y 2) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 1) (y 3) (hidden_neigh 1) (flag_neigh 0) (value 1))
    (tile (x 1) (y 4) (hidden_neigh 1) (flag_neigh 0) (value 1))
    (tile (x 2) (y 0) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 2) (y 1) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 2) (y 2) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 2) (y 3) (hidden_neigh 2) (flag_neigh 0) (value 2))
    (tile (x 2) (y 4) (hidden_neigh 1) (flag_neigh 0) (value -1))
    (tile (x 3) (y 0) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 3) (y 1) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 3) (y 2) (hidden_neigh 1) (flag_neigh 0) (value 1))
    (tile (x 3) (y 3) (hidden_neigh 4) (flag_neigh 0) (value 3))
    (tile (x 3) (y 4) (hidden_neigh 3) (flag_neigh 0) (value -1))
    (tile (x 4) (y 0) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 4) (y 1) (hidden_neigh 0) (flag_neigh 0) (value 0))
    (tile (x 4) (y 2) (hidden_neigh 1) (flag_neigh 0) (value 1))
    (tile (x 4) (y 3) (hidden_neigh 2) (flag_neigh 0) (value -1))
    (tile (x 4) (y 4) (hidden_neigh 2) (flag_neigh 0) (value -1))
    (val (x 4) (y 4) (v 2))

)



(defrule startup
    =>
    (printout t crlf "Minesweeper" crlf crlf)
    (printout t " 3x3 " crlf)
    (printout t "yoyoyo" crlf)
)



(defrule change_isBomb
    ?hh <- (decrement_hn (x ?x) (y ?y))
    ?gg <- (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?v))
    (test (neq ?h 0))
    =>
    
    (assert 
        (tile (x ?x) (y ?y) (hidden_neigh (+ ?h -1)) (flag_neigh (+ ?f 1)) (value ?v))
    )
    (printout t "decrement hn : " ?x " " ?y crlf)
    (printout t  "nilai awal : " ?h " " ?f " " ?v " "   crlf)
    (printout t  "ngebuka : " (+ ?h -1) " " (+ ?f 1)" "  ?v crlf)
    (printout t  crlf)
    (retract ?gg ?hh)
    
)

(defrule change_isBomb_all
    ?hh <- (decrement_hn_all (x ?x) (y ?y))

    ?gg1 <- (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value ?v1))
    (test (eq ?x1 (+ ?x -1)))
    (test (eq ?y1 (+ ?y -1)))
    ;(test (neq ?h1 0))

    ?gg2 <- (tile (x ?x2) (y ?y2) (hidden_neigh ?h2) (flag_neigh ?f2) (value ?v2))
    (test (eq ?x2 (+ ?x -1)))
    (test (eq ?y2 ?y))
    ;(test (neq ?h2 0))

    ?gg3 <- (tile (x ?x3) (y ?y3) (hidden_neigh ?h3) (flag_neigh ?f3) (value ?v3))
    (test (eq ?x3 (+ ?x -1)))
    (test (eq ?y3 (+ ?y 1)))
    ;(test (neq ?h3 0))

    ?gg4 <- (tile (x ?x4) (y ?y4) (hidden_neigh ?h4) (flag_neigh ?f4) (value ?v4))
    (test (eq ?x4 ?x))
    (test (eq ?y4 (+ ?y -1)))
    ;(test (neq ?h4 0))

    ?gg5 <- (tile (x ?x5) (y ?y5) (hidden_neigh ?h5) (flag_neigh ?f5) (value ?v5))
    (test (eq ?x5 ?x))
    (test (eq ?y5 (+ ?y 1)))
    ;(test (neq ?h5 0))

    ?gg6 <- (tile (x ?x6) (y ?y6) (hidden_neigh ?h6) (flag_neigh ?f6) (value ?v6))
    (test (eq ?x6 (+ ?x 1)))
    (test (eq ?y6 (+ ?y -1)))
    ;(test (neq ?h6 0))

    ?gg7 <- (tile (x ?x7) (y ?y7) (hidden_neigh ?h7) (flag_neigh ?f7) (value ?v7))
    (test (eq ?x7 (+ ?x 1)))
    (test (eq ?y7 ?y))
   ; (test (neq ?h7 0))

    ?gg8 <- (tile (x ?x8) (y ?y8) (hidden_neigh ?h8) (flag_neigh ?f8) (value ?v8))
    (test (eq ?x8 (+ ?x 1)))
    (test (eq ?y8 (+ ?y 1)))
    ;(test (neq ?h8 0))


    =>
    
    (assert 
        (tile (x ?x1) (y ?y1) (hidden_neigh (+ ?h1 -1)) (flag_neigh (+ ?f1 1)) (value ?v1))
        (tile (x ?x2) (y ?y2) (hidden_neigh (+ ?h2 -1)) (flag_neigh (+ ?f2 1)) (value ?v2))
        (tile (x ?x3) (y ?y3) (hidden_neigh (+ ?h3 -1)) (flag_neigh (+ ?f3 1)) (value ?v3))
        (tile (x ?x4) (y ?y4) (hidden_neigh (+ ?h4 -1)) (flag_neigh (+ ?f4 1)) (value ?v4))
        (tile (x ?x5) (y ?y5) (hidden_neigh (+ ?h5 -1)) (flag_neigh (+ ?f5 1)) (value ?v5))
        (tile (x ?x6) (y ?y6) (hidden_neigh (+ ?h6 -1)) (flag_neigh (+ ?f6 1)) (value ?v6))
        (tile (x ?x7) (y ?y7) (hidden_neigh (+ ?h7 -1)) (flag_neigh (+ ?f7 1)) (value ?v7))
        (tile (x ?x8) (y ?y8) (hidden_neigh (+ ?h8 -1)) (flag_neigh (+ ?f8 1)) (value ?v8))
    )
    (printout t "decrement hn ALLL : " ?x " " ?y crlf)
    ;(printout t  "nilai awal : " ?h1 " " ?f " " ?v " "   crlf)
    ;(printout t  "ngebuka : " (+ ?h1 -1) " " (+ ?f 1)" "  ?v crlf)
    (printout t  crlf)
    (retract ?gg1 ?gg2 ?gg3 ?gg4 ?gg5 ?gg6 ?gg7 ?gg8 ?hh)
    
)

(defrule change_isClear
    ?hh <- (decrement_fn (x ?x) (y ?y))
    ?gg <- (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?v))
    (test (neq ?h 0))
    =>
    (assert 
        (tile (x ?x) (y ?y) (hidden_neigh (+ ?h -1)) (flag_neigh ?f) (value ?v))
    )
    (printout t "decrement fn  " ?x " " ?y crlf)
    (printout t  "nilai awal : " ?h " " ?f " " ?v   crlf)
    (printout t  "ngebuka : " (+ ?h -1) " "  (+ ?f 1)" "  ?v crlf)
    (printout t  crlf)
    (retract ?gg ?hh)
)

(defrule change_isClear_all
    ?hh <- (decrement_fn_all (x ?x) (y ?y))

    ?gg1 <- (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value ?v1))
    (test (eq ?x1 (+ ?x -1)))
    (test (eq ?y1 (+ ?y -1)))
    ;(test (neq ?h1 0))

    ?gg2 <- (tile (x ?x2) (y ?y2) (hidden_neigh ?h2) (flag_neigh ?f2) (value ?v2))
    (test (eq ?x2 (+ ?x -1)))
    (test (eq ?y2 ?y))
    ;(test (neq ?h2 0))

    ?gg3 <- (tile (x ?x3) (y ?y3) (hidden_neigh ?h3) (flag_neigh ?f3) (value ?v3))
    (test (eq ?x3 (+ ?x -1)))
    (test (eq ?y3 (+ ?y 1)))
   ; (test (neq ?h3 0))

    ?gg4 <- (tile (x ?x4) (y ?y4) (hidden_neigh ?h4) (flag_neigh ?f4) (value ?v4))
    (test (eq ?x4 ?x))
    (test (eq ?y4 (+ ?y -1)))
   ; (test (neq ?h4 0))

    ?gg5 <- (tile (x ?x5) (y ?y5) (hidden_neigh ?h5) (flag_neigh ?f5) (value ?v5))
    (test (eq ?x5 ?x))
    (test (eq ?y5 (+ ?y 1)))
   ; (test (neq ?h5 0))

    ?gg6 <- (tile (x ?x6) (y ?y6) (hidden_neigh ?h6) (flag_neigh ?f6) (value ?v6))
    (test (eq ?x6 (+ ?x 1)))
    (test (eq ?y6 (+ ?y -1)))
    ;(test (neq ?h6 0))

    ?gg7 <- (tile (x ?x7) (y ?y7) (hidden_neigh ?h7) (flag_neigh ?f7) (value ?v7))
    (test (eq ?x7 (+ ?x 1)))
    (test (eq ?y7 ?y))
    ;(test (neq ?h7 0))

    ?gg8 <- (tile (x ?x8) (y ?y8) (hidden_neigh ?h8) (flag_neigh ?f8) (value ?v8))
    (test (eq ?x8 (+ ?x 1)))
    (test (eq ?y8 (+ ?y 1)))
    ;(test (neq ?h8 0))

    =>
    (assert 
        (tile (x ?x1) (y ?y1) (hidden_neigh (+ ?h1 -1)) (flag_neigh ?f1) (value ?v1))
        (tile (x ?x2) (y ?y2) (hidden_neigh (+ ?h2 -1)) (flag_neigh ?f2) (value ?v2))
        (tile (x ?x3) (y ?y3) (hidden_neigh (+ ?h3 -1)) (flag_neigh ?f3) (value ?v3))
        (tile (x ?x4) (y ?y4) (hidden_neigh (+ ?h4 -1)) (flag_neigh ?f4) (value ?v4))
        (tile (x ?x5) (y ?y5) (hidden_neigh (+ ?h5 -1)) (flag_neigh ?f5) (value ?v5))
        (tile (x ?x6) (y ?y6) (hidden_neigh (+ ?h6 -1)) (flag_neigh ?f6) (value ?v6))
        (tile (x ?x7) (y ?y7) (hidden_neigh (+ ?h7 -1)) (flag_neigh ?f7) (value ?v7))
        (tile (x ?x8) (y ?y8) (hidden_neigh (+ ?h8 -1)) (flag_neigh ?f8) (value ?v8))

    )
    (printout t "decrement fn ALLL   " ?x " " ?y crlf)
    ;(printout t  "nilai awal : " ?h " " ?f " " ?v   crlf)
    ;(printout t  "ngebuka : " (+ ?h -1) " "  (+ ?f 1)" "  ?v crlf)
    (printout t  crlf)
    (retract ?gg1 ?gg2 ?gg3 ?gg4 ?gg5 ?gg6 ?gg7 ?gg8 ?hh)
)


(defrule isClear
    (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?v))
    (test (eq ?v ?f))

    ?gg <- (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value ?v1))
    (test (eq ?v1 -1))

    (val (x ?x2) (y ?y2) (v ?v2))
    (and (test (eq ?x2 ?x1)) (test (eq ?y2 ?y1)))

    (or
        (and (test (eq ?x (+ ?x1 -1))) (test (eq ?y (+ ?y1 -1))) )
        (or 
            (and (test (eq ?x (+ ?x1 -1))) (test (eq ?y ?y1)) )
            (or 
                (and (test (eq ?x (+ ?x1 -1))) (test (eq ?y (+ ?y1 1))) )
                (or 
                    (and (test (eq ?x ?x1)) (test (eq ?y (+ ?y1 -1))) )
                    (or 
                        (and (test (eq ?x ?x1)) (test (eq ?y (+ ?y1 1))) )
                        (or 
                            (and (test (eq ?x (+ ?x1 1))) (test (eq ?y (+ ?y1 -1))) )
                            (or 
                                (and (test (eq ?x (+ ?x1 1))) (test (eq ?y ?y1)) )
                                (and (test (eq ?x (+ ?x1 1)))(test (eq ?y (+ ?y1 1))) )
                            )
                        )
                    )
                )
            )
        )
    )
    
    
    =>
    (retract ?gg)
    (assert (opened (x ?x1) (y ?y1))
            (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value ?v2))
            (decrement_fn_all (x ?x1) (y ?y1) )
            ;(decrement_fn (x (+ ?x1 -1)) (y (+ ?y1 -1)) )
            ;(decrement_fn (x (+ ?x1 -1)) (y ?y1) )
            ;(decrement_fn (x (+ ?x1 -1)) (y (+ ?y1 1)) )
;
            ;(decrement_fn (x ?x1) (y (+ ?y1 -1)) )
            ;(decrement_fn (x ?x1) (y (+ ?y1 1)) )
;
            ;(decrement_fn (x (+ ?x1 1)) (y (+ ?y1 -1)) )
            ;(decrement_fn (x (+ ?x1 1)) (y ?y1) )
            ;(decrement_fn (x (+ ?x1 1)) (y (+ ?y1 1)) )
    )
    
    (printout t "isClear:" crlf)
    (printout t  "sumber :  " ?x " " ?y crlf)
    (printout t  "ngebuka : " ?x1 " "  ?y1 crlf)
    (printout t  crlf)
)

(defrule isBomb
    (tile (x ?x) (y ?y) (hidden_neigh ?h) (flag_neigh ?f) (value ?v))
    (test (eq ?v (- ?h ?f)))
    

    ?gg <- (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value ?v1))
    (test (eq ?v1 -1))

    (or
        (and (test (eq ?x (+ ?x1 -1))) (test (eq ?y (+ ?y1 -1))) )
        (or 
            (and (test (eq ?x (+ ?x1 -1))) (test (eq ?y ?y1)) )
            (or 
                (and (test (eq ?x (+ ?x1 -1))) (test (eq ?y (+ ?y1 1))) )
                (or 
                    (and (test (eq ?x ?x1)) (test (eq ?y (+ ?y1 -1))) )
                    (or 
                        (and (test (eq ?x ?x1)) (test (eq ?y (+ ?y1 1))) )
                        (or 
                            (and (test (eq ?x (+ ?x1 1))) (test (eq ?y (+ ?y1 -1))) )
                            (or 
                                (and (test (eq ?x (+ ?x1 1))) (test (eq ?y ?y1)) )
                                (and (test (eq ?x (+ ?x1 1)))(test (eq ?y (+ ?y1 1))) )
                            )
                        )
                    )
                )
            )
        )
    )

   

    =>

    (retract ?gg)
    (assert (bomb (x ?x1) (y ?y1))
            (tile (x ?x1) (y ?y1) (hidden_neigh ?h1) (flag_neigh ?f1) (value -2))
            (decrement_hn_all (x ?x1) (y ?y1) )
            ;(decrement_hn (x (+ ?x1 -1)) (y (+ ?y1 -1)) )
            ;(decrement_hn (x (+ ?x1 -1)) (y ?y1) )
            ;(decrement_hn (x (+ ?x1 -1)) (y (+ ?y1 1)) )
;
            ;(decrement_hn (x ?x1) (y (+ ?y1 -1)) )
            ;(decrement_hn (x ?x1) (y (+ ?y1 1)) )
;
            ;(decrement_hn (x (+ ?x1 1)) (y (+ ?y1 -1)) )
            ;(decrement_hn (x (+ ?x1 1)) (y ?y1) )
            ;(decrement_hn (x (+ ?x1 1)) (y (+ ?y1 1)) )
    )
    
    (printout t "isBomb:"  crlf)
    (printout t  "sumber :  " ?x " " ?y crlf)
    (printout t  "ngebuka : " ?x1 " " ?y1 crlf)
    (printout t  crlf)
    
    ;;;(printout t  ?x1 ?y1 crlf)
)

