## Your tools

Your working directory, `{workdir}`, holds the talk transcripts: one markdown
file per talk, named `<talk-id>.md`. Each file starts with a short header,
followed by the transcript:

```
# <talk title (speaker, company — event)>
- talk: <talk-id>
- video: <YouTube link>
- published: <date>

<transcript text>
```

You can use Read, Grep and Glob on these files, and nothing else.

If a tool's output is too long, it is saved to a file and you are given its path;
you can Read that file.

In a claim, `talk` is the talk id: the file name without `.md`.
