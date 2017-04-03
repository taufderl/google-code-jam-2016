package main

import (
  "fmt"
  "io/ioutil"
  "strings"
  "strconv"
  "os"
)

func readInput(filename string) (data []int) {
  datain, _ := ioutil.ReadFile(filename)
  datastring := string(datain)
  x := strings.Split(datastring, "\n")
  for _, e := range x {
    j, _ := strconv.Atoi(e)
    data = append(data, j)
  }
  return
}


func analyzeNumber(x int) (last string) {
  fmt.Println(x)
  fmt.Println(x*2)
  os.Exit(0)
  return
}


func main() {
  numbers := readInput("A-small-practice.in")
  //numbers := readInput("A-large-practice.in")
  count := numbers[0]
  fmt.Printf("Read %v numbers\n", count)
  results := make(map[int]string)

  for i := 1; i<=count; i++ {
    results[i] = analyzeNumber(numbers[i])
  }

  for i := 1; i<=count; i++ {
    //fmt.Printf("Case #%v: %v (input: %v)\n",i, results[i], numbers[i])
  }
}