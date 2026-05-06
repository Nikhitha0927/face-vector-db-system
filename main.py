from crud import insert_face, find_closest_face

sample_vector = [0.1] * 128

print("Inserting data...")
insert_face("Nikhitha", sample_vector)

print("Searching match...")
result = find_closest_face(sample_vector)

if result:
    print("Matched person:", result.name)
else:
    print("No match found")