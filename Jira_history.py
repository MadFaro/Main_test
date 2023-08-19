[NeMo I 2023-08-19 15:42:12 mixins:170] Tokenizer SentencePieceTokenizer initialized with 128 tokens
[NeMo W 2023-08-19 15:42:12 modelPT:161] If you intend to do training or fine-tuning, please call the ModelPT.setup_training_data() method and provide a valid configuration file to setup the train data loader.
    Train config :
    manifest_filepath: null
    sample_rate: 16000
    batch_size: 16
    shuffle: true
    num_workers: 8
    pin_memory: true
    use_start_end_token: ''
    trim_silence: false
    max_duration: 20.0
    min_duration: 0.1
    is_tarred: false
    tarred_audio_filepaths: null
    shuffle_n: 2048
    bucketing_strategy: synced_randomized
    bucketing_batch_size: null

[NeMo W 2023-08-19 15:42:12 modelPT:168] If you intend to do validation, please call the ModelPT.setup_validation_data() or ModelPT.setup_multiple_validation_data() method and provide a valid configuration file to setup the validation data loader(s).
    Validation config :
    manifest_filepath: null
    sample_rate: 16000
    batch_size: 16
    shuffle: false
    num_workers: 8
    pin_memory: true
    use_start_end_token: ''

[NeMo W 2023-08-19 15:42:12 modelPT:174] Please call the ModelPT.setup_test_data() or ModelPT.setup_multiple_test_data() method and provide a valid configuration file to setup the test data loader(s).
    Test config :
    manifest_filepath: null
    sample_rate: 16000
    batch_size: 16
    shuffle: false
    num_workers: 8
    pin_memory: true
    use_start_end_token: ''

[NeMo I 2023-08-19 15:42:12 features:289] PADDING: 0
[NeMo I 2023-08-19 15:42:13 save_restore_connector:249] Model EncDecCTCModelBPE was successfully restored from C:\Users\TologonovAB\Desktop\nemo_model\stt_ru_conformer_ctc_large.nemo.
Traceback (most recent call last):
  File "Nemo.py", line 26, in <module>
    transcriptions = asr_model.transcribe([audio_list])
  File "C:\Python38\lib\site-packages\torch\utils\_contextlib.py", line 115, in decorate_context
    return func(*args, **kwargs)
  File "C:\Python38\lib\site-packages\nemo\collections\asr\models\ctc_models.py", line 196, in transcribe
    temporary_datalayer = self._setup_transcribe_dataloader(config)
  File "C:\Python38\lib\site-packages\nemo\collections\asr\models\ctc_bpe_models.py", line 171, in _setup_transcribe_dataloader
    temporary_datalayer = self._setup_dataloader_from_config(config=DictConfig(dl_config))
  File "C:\Python38\lib\site-packages\nemo\collections\asr\models\ctc_bpe_models.py", line 92, in _setup_dataloader_from_config
    dataset = audio_to_text_dataset.get_audio_to_text_bpe_dataset_from_config(
  File "C:\Python38\lib\site-packages\nemo\collections\asr\data\audio_to_text_dataset.py", line 827, in get_audio_to_text_bpe_dataset_from_config
    dataset = get_bpe_dataset(config=config, tokenizer=tokenizer, augmentor=augmentor)
  File "C:\Python38\lib\site-packages\nemo\collections\asr\data\audio_to_text_dataset.py", line 222, in get_bpe_dataset
    dataset = audio_to_text.AudioToBPEDataset(
  File "C:\Python38\lib\site-packages\nemo\collections\asr\data\audio_to_text.py", line 690, in __init__
    super().__init__(
  File "C:\Python38\lib\site-packages\nemo\collections\asr\data\audio_to_text.py", line 452, in __init__
    self.manifest_processor = ASRManifestProcessor(
  File "C:\Python38\lib\site-packages\nemo\collections\asr\data\audio_to_text.py", line 140, in __init__
    self.collection = collections.ASRAudioText(
  File "C:\Python38\lib\site-packages\nemo\collections\common\parts\preprocessing\collections.py", line 223, in __init__
    for item in manifest.item_iter(manifests_files):
  File "C:\Python38\lib\site-packages\nemo\collections\common\parts\preprocessing\manifest.py", line 80, in item_iter
    item = parse_func(line, manifest_file)
  File "C:\Python38\lib\site-packages\nemo\collections\common\parts\preprocessing\manifest.py", line 103, in __parse_item
    item['audio_file'] = get_full_path(audio_file=item['audio_file'], manifest_file=manifest_file)
  File "C:\Python38\lib\site-packages\nemo\collections\common\parts\preprocessing\manifest.py", line 187, in get_full_path
    return [
  File "C:\Python38\lib\site-packages\nemo\collections\common\parts\preprocessing\manifest.py", line 188, in <listcomp>
    get_full_path(
  File "C:\Python38\lib\site-packages\nemo\collections\common\parts\preprocessing\manifest.py", line 231, in get_full_path
    raise ValueError(f'Unexpected audio_file type {type(audio_file)}, audio_file {audio_file}.')
ValueError: Unexpected audio_file type <class 'float'>, audio_file -8.714778232388198e-09.
