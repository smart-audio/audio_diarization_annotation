# Audio Diarization Annotation
Audio Diarization Annotation tool based on library wavesurfer.js.
Serves by Flask.

![](./art/Peek%202019-09-19%2022-05.gif)

## How to use
`python app/app.py <working_dir>`
`working_dir` directory is like the following `demo_dir`.
```
├── demo_dir
│   ├── annotation
│   │   └── demo1.json
│   └── audio
│       └── demo1.mp3
```

## Requirements
- Python 3
- Flask