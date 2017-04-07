import os
import pickle
import numpy as np

np.random.seed(142857)


class Util:
    @staticmethod
    def get_and_pop(dic, key, default):
        try:
            val = dic[key]
            dic.pop(key)
        except KeyError:
            val = default
        return val

    @staticmethod
    def callable(obj):
        _str_obj = str(obj)
        if callable(obj):
            return True
        if "<" not in _str_obj and ">" not in _str_obj:
            return False
        if _str_obj.find("function") >= 0 or _str_obj.find("staticmethod") >= 0:
            return True


def gen_dataset(dat_path):
    if not os.path.isfile(dat_path):
        print("\nGenerating Dataset...")
        folders = os.listdir("_Data")
        label_dic = [folder for folder in folders if os.path.isdir(os.path.join("_Data", folder))]
        folders_path = [os.path.join("_Data", folder) for folder in label_dic]
        x, y = [], []
        for i, folder in enumerate(folders_path):
            for txt in os.listdir(folder):
                with open(os.path.join(folder, txt), "r", encoding="utf-8") as file:
                    try:
                        x.append(file.read().strip().split())
                        y.append(i)
                    except Exception as err:
                        print(err)
        np.save(os.path.join("_Data", "LABEL_DIC.npy"), label_dic)
        with open(dat_path, "wb") as file:
            pickle.dump((x, y), file)
        print("Done")
