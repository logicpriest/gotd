# Gender of the Day Discord Bot Code

## Instructions
1. Clone the repo
2. Build the container image `podman build -f Dockerfile -t gender-bot .`
3. Run with the TOKEN env variable `podman run -it -e TOKEN='<token>' --name gender-bot gender-bot`
4. Alternatively - `podman run --label "io.containers.autoupdate=image" -it -e TOKEN='<token>' --name gender-bot gender-bot`
* docker works in place of podman

