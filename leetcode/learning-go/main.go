package main

import "fmt"


func main () {
	fmt.Println("Hello!")

	fmt.Println(concact("Hello ", "Naman"))
}



// type comes after the name of the variable.... kind of the reverse of java....
func concact(s1 , s2 string) string {
	return s1 + s2

}





