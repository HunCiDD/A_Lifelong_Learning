# 构建：使用golang 制定版本
FROM golang:alpine as build

# 容器环境变量添加
ENV GO111MODULE=auto
ENV GOPROXY=https://goproxy.cn,direct

# 设置当前工作区
WORKDIR /go/src
# 把全部文件添加到/go/release目录
ADD http_server.go /go/src
# 编译: http_server.go编译为可执行的二进制文件
RUN cd /go/src && go build -o http_server

# 运行: 使用 alpine 作为基础镜像
FROM alpine:latest as prod
WORKDIR /app
# 在build阶段, 复制时区配置到镜像的
COPY --from=build /go/src/http_server /app/
# 设置端口
EXPOSE 8080
CMD ["/app/http_server"]