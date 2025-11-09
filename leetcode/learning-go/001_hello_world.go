package main // you need this....

import "fmt"
import "errors"

func main() {
    fmt.Println("This is going to be very cool!")

    username := "naman0r"
    password := "110100010101"

    fmt.Println("Auth basic: ", username + ":" + password)

    mul, div, err := calculator(10, 0)

    fmt.Println(mul, div, err) // shows the errors.....

    mul, div, err = calculator(10, 2) // this should work


    fmt.Println(mul, div, err) // this should work
}


func calculator ( a, b int) (mul, div int, err error) {

    // this is called an early return or guard clause. it is a design decision to prevent unnesesary compute. 
    if (b == 0) {
        return 0, 0, errors.New("division by zero")
    }
    mul = a * b // since we have alread declared this variable in the signature, we do not have to force to infer a type using 
    // := or give it a type here.....
    div = a / b
    return mul, div, nil
}


