def exists_word(word, instance):
    """Aqui irá sua implementação"""
    result = list()
    occurrences = list()
    for index in range(len(instance)):
        search = instance.search(index)
        lines = search['linhas_do_arquivo']
        for index, line in enumerate(lines):
            if word.lower() in line.lower():
                occurrences.append({"linha": index + 1})

        if len(occurrences) >= 1:
            search_result = {
                "palavra": word,
                "arquivo": search["nome_do_arquivo"],
                "ocorrencias": occurrences
            }
            result.append(search_result)

    return result  

def search_by_word(word, instance):
    """Aqui irá sua implementação"""
    