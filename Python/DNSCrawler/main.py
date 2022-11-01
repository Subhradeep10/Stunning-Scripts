from dns import resolver


def get_records(domain):
    record_types = ["a", "mx", "txt", "cname"]
    records = []
    searcher = resolver.Resolver()

    for record_type in record_types:
        try:
            search = searcher.resolve(
                domain if record_type != "cname" else f"www.{domain}", record_type
            )
            for data in search:
                if record_type == "cname":
                    records.append(
                        "www" f" 14400s {str(record_type).upper()} {data}"
                    )
                else:
                    records.append(f" 14400s {str(record_type).upper()} {data}")
        except:
            print(f'Failed to search the record type {record_type}')
    return records


records = get_records('bbc.com')

for r in records:
    print(r)
