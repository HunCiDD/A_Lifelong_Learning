package main

import (
	"fmt"
	"net/http"
	"os"
	"strings"
)

type MyHandler struct{}

func (m *MyHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	var code string = "200"
	var msg string
	var content []string
	if r.URL.Path == "/healthz" {
		code = "200"
		msg = "<h1>200, Hello World！</h1>"
	} else {
		code = "404"
		msg = "<h1>404, 您访问的页面不存在！</h1>"
	}
	content = append(content, code)
	content = append(content, msg)
	for k, value := range r.Header {
		tmp := "<h3>[" + k + "]" + strings.Join(value, " ") + "</h3>"
		content = append(content, tmp)
	}
	version := os.Getenv("VERSION")
	version = "<h3>Version:" + version + "</h3>"
	content = append(content, version)
	w.Write([]byte(strings.Join(content, "\n")))
	fmt.Printf("客户端IP[%s],HTTP返回码[%s]\n", r.Host, code)
}

func main() {
	mh := MyHandler{}
	server := http.Server{
		Addr:    "localhost:8080",
		Handler: &mh,
	}
	server.ListenAndServe()
}
