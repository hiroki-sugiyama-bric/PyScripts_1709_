from form_info_util import extract_infos

# PATH_1 = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/snippets/login_nf_forms_171005.txt'
PATH_1 = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/snippets/login_fp_forms_171006.txt'
PATH_2 = '/Users/hirokisugiyama/Work/NTTTX/NTTTX_201709_/data/snippets/non_login_forms_with_login_buttons_171005.txt'


def compare():
    infos_1 = extract_infos(PATH_1)
    infos_2 = extract_infos(PATH_2)

    # 要素がdictなのでsetでの比較はできない
    duplicates = [i for i in infos_1 if i in infos_2]
    print(len(duplicates))
    for dup in duplicates:
        print(dup)


if __name__ == '__main__':
    compare()
