import re


def get_limit(strings_list):
	result = list()

	for string in strings_list:
		if re.search(r'публикац', string.lower()):
			result = strings_list[0:strings_list.index(string)]

	return result


def verify_resources(url):
	list_of_res = ['scholar.google', 'zbmath.org', 'www.ams.org', 'elibrary.ru',
	 'istina.msu.ru', 'orcid.org', 'www.researcherid.com', 'scopus', 'esearchgate']

	for res in list_of_res:
		pattern = re.compile(res)
		if pattern.search(url) is not None:
			return url

	return None


def verify_emails(string):
	if re.search(r'.+@.+', string) is not None:
		return string
	else:
		return None


def verify_position(strings_list):
	patterns = ['профессор', 'академик ран', 'доцент', 'преподаватель']

	for string in strings_list:
		for p in patterns:
			pattern = re.compile(p)
			if pattern.search(string.lower()) is not None:
				return string


def verify_sci_degree(strings_list):
	patterns = ['доктор', 'кандидат']

	for string in strings_list:
		for p in patterns:
			pattern = re.compile(p)
			if pattern.search(string.lower()) is not None:
				return string


def verify_keywords(strings_list):
	pattern = re.compile('ключевые слова')

	for string in strings_list:
		if pattern.search(string.lower()) is not None:
			return strings_list[strings_list.index(string) + 1]





