# ShareX Uploader

[ShareX](https://getsharex.com/) Image Uploader made to be hosted in a Docker container. [ShareX](https://getsharex.com/) is an Open Source screenshotting tool. It let's you configure it to uploade your screenshots to large image hosting sites, or to your own web instance to flex on your friends. This allows you to have your own image links such as `https://i.example.com/sdflkj3497.png`.

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

## Building docker image

You can build the docker image from source by cloning this repo, and then run the command below.

```console
docker build --no-cache -t sharex-uploader .
```

Then you can set up the container in the same way as te previous section. Replace `jazper/sharex-uploader:latest` with `sharex-uploader` and the you should be good to go.

## Configuring ShareX

In the ShareX main menu, click the "Destinations" tab in the left hand side panel. Then choose the option at the buttom "Custom uploader settings". Choose the option to import a config from a URl, and paste this URL into the text field: `https://raw.githubusercontent.com/j4asper/ShareX-Uploader/main/sharex-config.json`.  
Then the base config should be loaded now, and you can now replace all instances of `example.com` to your domain. Remember to include the port of your docker container if it's different from `80` or `443`.
