from app.services.intelligence.unified_trends import (
    get_unified_trends
)

for item in get_unified_trends():

    print(item)