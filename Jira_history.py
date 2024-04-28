class_weights = {}
total_samples = len(y)
for cls_idx, cls in enumerate(np.unique(y)):
    cls_samples = np.sum(y == cls)
    weight = total_samples / (len(np.unique(y)) * cls_samples)
    class_weights[cls_idx] = weight
