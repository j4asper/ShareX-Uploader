<a href="https://github.com/j4asper/ShareX-Uploader/blob/main/LICENSE"><img src="https://img.shields.io/github/license/j4asper/sharex-uploader?style=for-the-badge"></a> <a href="https://hub.docker.com/r/jazper/sharex-uploader"><img src="https://img.shields.io/docker/pulls/jazper/sharex-uploader?style=for-the-badge&logo=Docker"></a> <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&label=Python&logo=Python"></a>

# ShareX Uploader

[ShareX](https://getsharex.com/) is a free and open source program that lets you capture or record any area of your screen and share it with a single press of a key. It also allows uploading images, text or other types of files to many supported destinations you can choose from.

If you choose to use this ShareX Uploader, you will be able to upload images to your own server, and have cool links to them such as this one `https://i.jazper.dk/EsCJgx.png`.

![Demo Image](https://i.jazper.dk/EsCJgx.png)

## Table of contents

- [Setting up the docker container](#setting-up-the-docker-container)
  - [Environment Variables](#environment-variables)
- [Building docker image](#building-docker-image)
- [Configuring ShareX](#configuring-sharex)
  - [Image and File Uploader](#image-and-file-uploader)
  - [URL Shortener](#url-shortener)
- [To-Do](#to-do)

## Setting up the docker container

Simplest way to run the ShareX Uploader. Replace `password` with the auth password you want to use, to prevent people from uploading stuff to your sharex uploader instance. You can also remove `-e TOKEN=password` to disable upload authentication, this will allow everyone to upload to you instance.  
If you want the instance to run on port 80, then change `8000:8000` to `80:8000`.

```console
docker run -d -e TOKEN=password -p 8000:8000 jazper/sharex-uploader:latest
```

You may want to create a shared volume for your docker container to be able to access the images on the docker instance easier, by binding the `images` folder to a folder on your host machine. Make sure to edit `/path/to/your/folder`. This will be the folder that contains all the images uploaded to the sharex uploader instance.

```console
docker run -d -p 8000:8000 -v /ShareX-Uploader/images:/path/to/your/folder jazper/sharex-uploader:latest
```

### Environment Variables

Environment Variables you may want to change. It is highly recommended to change the TOKEN, to prevent spam uploads to your instance.

| Name                | Requirement | Value  | Default Value | Description                                                                              |
|---------------------|-------------|--------|--------|-------------------------------------------------------------------------------------------------|
| TOKEN               | Optional    | string | `None` | Token needed to be able to upload images, if not set, everyone can upload to the server.        |
| MAX_FILENAME_LENGTH | Optional    | int    | 6      | Length of image names 4 or above is recommended.                                                |
| MAX_UPLOAD_SIZE     | Optional    | int    | 10     | Max size of uploaded files in MB, you should you increase this if you plan to upload videoes    |
| SHORT_URL_LENGTH    | Optional    | int    | 4      | Length of shortened url "codes"                                                                 |

The docker run command would be the following, if you were to set all the environment vars to the default value.

```console
docker run -d -e TOKEN=your-password-here -e MAX_FILENAME_LENGTH=6 -e MAX_UPLOAD_SIZE=10 -p 8000:8000 jazper/sharex-uploader:latest
```

You can change the values as you wish, or remove them if you just want to use the default value.

## Building docker image

You can build the docker image from source by cloning this repo, and then run the command below.

```console
docker build --no-cache -t sharex-uploader .
```

Then you can set up the container in the same way as te previous section. Replace `jazper/sharex-uploader:latest` with `sharex-uploader` and the you should be good to go.

## Configuring ShareX

### Image and File Uploader

In the ShareX main menu, click the "Destinations" tab in the left hand side panel. Then choose the option at the buttom "Custom uploader settings". Choose the option to import a config from a URL, and paste this URL into the text field: `https://raw.githubusercontent.com/j4asper/ShareX-Uploader/main/sharex-configs/image%20and%20file%20uploader.json`.  
Then the base config should be loaded now, and you can now replace all instances of `example.com` to your domain. Remember to include the port of your docker container if it's different from `80` or `443`.
Now to use the custom uploader, click the "Destinations" tab again, then when hovering over "Image uploader" you can select "Custom Image Uploader". You can also use the custom image uplaoder to upload files, when in the "Destinations", select "File uploader" and then select "Custom File Uploader", this will use the image uploader as if it were a file uploader.

### URL Shortener

Go to the Custom Uploader Settings, the same way as in the above section. Then import a config from URL and paste this link into the text field: `https://raw.githubusercontent.com/j4asper/ShareX-Uploader/main/sharex-configs/url%20shortener.json`. Remember to change `example.com` to fit your own domain.
Then in the Destinations tab, hover over the URL Shortener, and select Custom URL Shortener.

## To-Do

- [ ] Add Delete endpoint with token authentication (Probably with web UI)
- [x] Add URL-Shortener functionality
- [ ] Add pastebin-like functionality
