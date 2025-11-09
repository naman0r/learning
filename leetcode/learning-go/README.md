## Go

this is my attempt of learning GoLang.....

```go


```

## Why go?

- go is a compiled language.... which makes it a lot faster than any interpreted lanugage.
- GoLang has a really fast compilation speed.

Go (Golang) has several advantages over other popular programming
languages that make it a powerful and attractive choice for many
developers and projects:

1. Simplicity and ease of learning: Go was designed with the goal of
   having an easy-to-understand syntax, which makes it relatively simple to
   learn for developers already familiar with other programming languages.
   The language emphasizes simplicity in both its design and code
   organization.

2. Concurrency: Go offers built-in support for concurrent programming
   through goroutines (lightweight threads) and channels (synchronized
   communication between goroutines). This makes it easier to write
   concurrent code, which is critical for modern applications that require
   scalable performance.

3. Garbage collection: Go has automatic memory management via a garbage
   collector. This eliminates the need for manual memory allocation and
   deallocation, reducing the risk of memory leaks and making it simpler to
   write error-free code.

4. Performance: Go is known for its high performance and low overhead due
   to its close alignment with machine architecture. The language's focus on
   static typing, small function signatures, minimal runtime, and efficient
   data structures contribute to this performance advantage.

5. Cross-platform: Go supports cross-platform development by offering a
   single compiled binary that can run on multiple operating systems without
   modification. This simplifies the deployment process and reduces the need
   for platform-specific code.

6. Standard library: Go's standard library is comprehensive and
   well-designed, providing developers with many useful functions and
   packages for common tasks such as working with concurrency, web
   frameworks, database connections, and more.

7. Strong community and ecosystem: The Go language has a thriving and
   active community of developers who contribute to its growth and
   improvement through open-source projects, libraries, tools, and resources.
   This strong ecosystem helps ensure that Go remains relevant and evolves
   over time.

## Running shared code:

write code in go -> build the go code -> creates a .exe file -> others can run it without needing go installed in their computer (not the case for python, java, etc. )

compile time error:

```go

package main

import "fmt"

func main() {
   fmt.println("noclosingquote)
}

```

## IN GO, VARIABLES ARE PASSED BY VALUE AND NOT BY REFERENCE, WHICH IS A VERY IMPORTANT DISTINCTION BERWEEN JAVA AND GO

so mutation functions ????? do not exist?????
