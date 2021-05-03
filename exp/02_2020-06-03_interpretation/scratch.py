

workdir = '24_2021-04-27_run'
ann_index = 0
ann = target_anns[0]




for i in range(len(histone_signal.track_names)):
    feature_name = segtools_trackname_mapping[histone_signal.track_names[i]].upper()
    if feature_name in histone_features:
        print(i)
        print(histone_signal.track_names[i])
        print(feature_name)
