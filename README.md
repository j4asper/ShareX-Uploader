<a href="https://github.com/j4asper/ShareX-Uploader/blob/main/LICENSE"><img src="https://img.shields.io/github/license/j4asper/sharex-uploader?style=for-the-badge"></a> <a href="https://hub.docker.com/r/jazper/sharex-uploader"><img src="https://img.shields.io/docker/pulls/jazper/sharex-uploader?style=for-the-badge&logo=Docker"></a> <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&label=Python&logo=Python"></a>

# ShareX Uploader

[ShareX](https://getsharex.com/) Image Uploader made to be hosted in a Docker container. [ShareX is an Open Source screenshotting tool](https://getsharex.com/). It let's you configure it to uploade your screenshots to large image hosting sites, or to your own web instance to flex on your friends. This allows you to have your own image links such as `https://i.example.com/Ml9dGI.png`.  

This ShareX Uploader supports image uploading and file uploading functionality.  

## Table of contents

- [Setting up the docker container](#setting-up-the-docker-container)
  - [Environment Variables](#environment-variables)
- [Building docker image](#building-docker-image)
- [Configuring ShareX](#configuring-sharex)
- [To-Do](#to-do)

## Setting up the docker container

Simplest way to run the ShareX Uploader. Replace `password` with the auth password you want to use, to prevent people from uploading stuff to your sharex uploader instance. You can also remove `-e TOKEN=password` to disable upload authentication, this will allow everyone to upload to you instance.  
If you want the instance to run on port 80, then change `8000:8000` to `80:8000`.

```console
docker run -d -e TOKEN=password -p 8000:8000 jazper/sharex-uploader:latest
```

You may want to create a shared volume for your docker container to be able to access the images on the docker instance easier, by binding the `images` folder to a folder on your host machine. Make sure to edit `/path/to/your/folder`. This will be the folder that contains all the images uploaded to the sharex uploader instance.

```console
docker run -d -e TOKEN=password -p 8000:8000 -v /ShareX-Uploader/images:/path/to/your/folder jazper/sharex-uploader:latest
```

### Environment Variables

Environment Variables you may want to change. It is highly recommended to change the TOKEN, to prevent spam uploads to your instance.

| Name                | Value  | Description                                                                              |
|---------------------|--------|------------------------------------------------------------------------------------------|
| TOKEN               | string | Token needed to be able to upload images, if not set, everyone can upload to the server. |
| MAX_FILENAME_LENGTH | int    | Length of image names 4 or above is recommended. Default is 6.                           |

## Building docker image

You can build the docker image from source by cloning this repo, and then run the command below.

```console
docker build --no-cache -t sharex-uploader .
```

Then you can set up the container in the same way as te previous section. Replace `jazper/sharex-uploader:latest` with `sharex-uploader` and the you should be good to go.

## Configuring ShareX

In the ShareX main menu, click the "Destinations" tab in the left hand side panel. Then choose the option at the buttom "Custom uploader settings". Choose the option to import a config from a URl, and paste this URL into the text field: `https://raw.githubusercontent.com/j4asper/ShareX-Uploader/main/sharex-config.json`.  
Then the base config should be loaded now, and you can now replace all instances of `example.com` to your domain. Remember to include the port of your docker container if it's different from `80` or `443`.

## To-Do

- [ ] Add Delete endpoint with token authentication (Probably with web UI)
- [ ] Add pastebin-like functionality
