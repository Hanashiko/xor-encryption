import codecs

def input_data() -> tuple:
	original_text: str = input("Введіть оригінальний текст: ")
	gama: int = input("Введіть гаму: ")
	return original_text, gama

def text_to_ascii(text: str) -> list:
	encoded_text = codecs.encode(text, "windows-1251")
	result_list: list(int) = list(encoded_text)
	return result_list

def ascii_to_text(ascii_list: list) -> str:
	decode_text = codecs.decode(bytes(ascii_list), "windows-1251")
	return decode_text

def decimal_to_binary(number: int) -> int:
	return "{0:b}".format(int(number))

def decimal_list_to_binary(decimals: list) -> list:
	binarys: list(int) = []
	for number in decimals:
		binarys.append(decimal_to_binary(number))
	return binarys

def xor(number_1: int, number_2: int) -> int:
	return number_1 ^ number_2

def xor_list(numbers: list, gama: int) -> list:
	result_list: list(int) = []
	for number in numbers:
		result_list.append(xor(int(number), int(gama)))
	return result_list

def list_to_str(original_list: list) -> str:
	result_string: str = ""
	for item in original_list:
		result_string += f"{str(item)}, "
	return result_string[:-2]

def main() -> None:
	text: str = ""
	gama: int = 0
	text, gama = input_data()

	print(f"\nОригінальний текст: {text}\nГама: {gama}")

	text_ascii: list(int) = text_to_ascii(text)
	print(f"Ваш текст переведений в ascii: {list_to_str(text_ascii)}")

	text_binary: list(int) = decimal_list_to_binary(text_ascii)
	print(f"ASCII значення вашого тексту переведене в двійковий код: {list_to_str(text_binary)}")

	gama_binary: int = decimal_to_binary(gama)
	print(f"Гама переведена в двійковий код: {gama_binary}")

	cipher_ascii: list(int) = xor_list(text_ascii, gama)
	print(f"ASCII значення після виконаня операції XOR: {list_to_str(cipher_ascii)}")

	cipher_binary: list(int) = decimal_list_to_binary(cipher_ascii)
	print(f"Зашифрований текст в двійковому вигляді: {list_to_str(cipher_binary)}")

	cipher_text: str = ascii_to_text(cipher_ascii)
	print(f"Зашифрований текст в звичайному для людей вигляді: {cipher_text}")


if __name__ == "__main__":
	main()
