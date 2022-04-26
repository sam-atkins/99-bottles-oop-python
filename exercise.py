class Bottles:
    def verse(self, number):
        if number == 2:
            return (
                "2 bottles of beer on the wall, 2 bottles of beer.\n"
                "Take one down and pass it around, 1 bottle of beer on the wall."
            )
        if number == 1:
            return (
                "1 bottle of beer on the wall, 1 bottle of beer.\n"
                "Take it down and pass it around, no more bottles of beer on the wall."
            )
        if number == 0:
            return (
                "No more bottles of beer on the wall, no more bottles of beer.\n"
                "Go to the store and buy some more, 99 bottles of beer on the wall."
            )

        return (
            f"{number} bottles of beer on the wall, {number} bottles of beer.\n"
            f"Take one down and pass it around, {number -1} bottles of beer on the wall."
        )

    def verses(self, start_number, end_number):
        verses_str = ""
        for num in reversed(range(end_number, start_number + 1)):
            verses_str += self.verse(num)
            if num != end_number:
                verses_str += "\n\n"

        return verses_str

    def song(self):
        start = 99
        end = 0
        return self.verses(start, end)
