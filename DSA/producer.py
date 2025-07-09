from kafka import KafkaProducer
import json
import time
import datetime
import random

status = True
list1=["A","B","C","D"]
# Define the Kafka producer
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)


# Function to produce messages
def produce_messages():
    global status
    while status:


        message2 = {
              "events": [
                {
                  "ab_test": "75817:1|113272:0|61853:0|47989:1|70712:0|102245:0|62403:1|60412:1|117812:1|120676:1|62591:0|113632:1|101168:0|116206:0|66480:0|100390:0|76965:1|110385:1|65556:0|48145:0|129832:2",
                  "adid": "df03f2b6-4eb2-41a0-9c21-76da0891f0ff",
                  "appid": "IPTV",
                  "av": "1.15.1",
                  "bn": "151",
                  "brand": "Amlogic",
                  "did": "40f15638fa7eb4ed",
                  "dname": "Amlogic qurra",
                  "dt": "STB",
                  "event_type": "click",
                  "firebase_instance_id": "63fff99c098b83b92e62c1920e640285",
                  "lc": "en|te",
                  "model": "qurra",
                  "nct": "0",
                  "nq": "-1",
                  "nt": "0",
                  "os": "Android",
                  "ov": "34",
                  "profileId": "",
                  "sId": "40f15638fa7eb4ed",
                  "ts": "1722427823110",
                  "uid": "vuH1osp61U5uH7lRX0"
                }
              ],
              "id": "994f8281-e035-4cb5-a69e-ec9ae6287ea9",
              "ts": "1722427823500"
            }

        # Create a sample message
        message1 = { "service": 200, "userid": random.choice(list1),"order_time": (int(str(time.time()).split(".")[0])*1000), "order_date": str(datetime.datetime.now(datetime.timezone.utc))[:-9] ,"properties": "hi" }

        message = {"service": 200, "userid": random.choice(list1),"order_time": (int(str(time.time()).split(".")[0])*1000), "order_date": str(datetime.datetime.now(datetime.timezone.utc))[:-9] ,"properties": [{"A":"data","A1":"data2"},{"B":"data1"},{"NA":"NA"}]}
        # Send the message to the 'output-topic' Kafka topic
        # producer.send('flink-test', message)
        message3 = {
                "events": [
                    {
                        "ab_test": "75817:1|113272:0|61853:0|47989:1|70712:0|102245:0|62403:1|60412:1|117812:1|120676:1|62591:0|113632:1|101168:0|116206:0|66480:0|100390:0|76965:1|110385:1|65556:0|48145:0|129832:2",
                        "adid": "df03f2b6-4eb2-41a0-9c21-76da0891f0ff",
                        "appid": "IPTV",
                        "av": "1.15.1",
                        "bn": "151",
                        "brand": "Amlogic",
                        "did": "40f15638fa7eb4ed",
                        "dname": "Amlogic qurra",
                        "dt": "STB",
                        "event_type": "click",
                        "firebase_instance_id": "63fff99c098b83b92e62c1920e640285",
                        "lc": "en|te",
                        "meta": {
                            "box_type": "iptv",
                            "source_of_stream": "1 | Home.screen_visible.none.none.none.none.none.none.none | none.screen_visible.none.none.none.none.none.none.none | none.click.tile_click.none.1.1.none.none.com.amazon.amazonvideo.livingroom",
                            "asset_position": "1",
                            "app_version": "1.15.1:151",
                            "box_model": "bx:1.2.3",
                            "content_id": "com.amazon.amazonvideo.livingroom",
                            "action": "tile_click",
                            "firmware": "fw:1.2.3",
                            "rail_position": "1"
                        },
                        "model": "qurra",
                        "nct": "0",
                        "nq": "-1",
                        "nt": "0",
                        "os": "Android",
                        "ov": "34",
                        "profileId": "",
                        "sId": "40f15638fa7eb4ed",
                        "ts": "1722427823110",
                        "uid": "vuH1osp61U5uH7lRX0"
                    },
                    {
                        "ab_test": "75817:1|113272:0|61853:0|47989:1|70712:0|102245:0|62403:1|60412:1|117812:1|120676:1|62591:0|113632:1|101168:0|116206:0|66480:0|100390:0|76965:1|110385:1|65556:0|48145:0|129832:2",
                        "adid": "df03f2b6-4eb2-41a0-9c21-76da0891f0ff",
                        "appid": "IPTV",
                        "av": "1.15.1",
                        "bn": "151",
                        "brand": "Amlogic",
                        "did": "40f15638fa7eb4ed",
                        "dname": "Amlogic qurra",
                        "dt": "STB",
                        "event_type": "click",
                        "firebase_instance_id": "63fff99c098b83b92e62c1920e640285",
                        "lc": "en|te",
                        "meta": {
                            "app_name": "Prime Video",
                            "box_type": "iptv",
                            "source_of_stream": "1 | Home.screen_visible.none.none.none.none.none.none.none | none.screen_visible.none.none.none.none.none.none.none | none.click.tile_click.none.1.1.none.none.com.amazon.amazonvideo.livingroom | none.click.app_click.none.1.none.none.none.none",
                            "app_version": "1.15.1:151",
                            "box_model": "bx:1.2.3",
                            "action": "app_click",
                            "firmware": "fw:1.2.3",
                            "rail_position": "1"
                        },
                        "model": "qurra",
                        "nct": "0",
                        "nq": "-1",
                        "nt": "0",
                        "os": "Android",
                        "ov": "34",
                        "profileId": "",
                        "sId": "40f15638fa7eb4ed",
                        "ts": "1722427823112",
                        "uid": "vuH1osp61U5uH7lRX0"
                    },
                    {
                        "ab_test": "75817:1|113272:0|61853:0|47989:1|70712:0|102245:0|62403:1|60412:1|117812:1|120676:1|62591:0|113632:1|101168:0|116206:0|66480:0|100390:0|76965:1|110385:1|65556:0|48145:0|129832:2",
                        "adid": "df03f2b6-4eb2-41a0-9c21-76da0891f0ff",
                        "appid": "IPTV",
                        "av": "1.15.1",
                        "bn": "151",
                        "brand": "Amlogic",
                        "did": "40f15638fa7eb4ed",
                        "dname": "Amlogic qurra",
                        "dt": "STB",
                        "event_type": "click",
                        "firebase_instance_id": "63fff99c098b83b92e62c1920e640285",
                        "lc": "en|te",
                        "meta": {
                            "thumbnail": "no",
                            "app_version": "1.15.1:151",
                            "box_model": "bx:1.2.3",
                            "content_id": "com.amazon.amazonvideo.livingroom",
                            "package_id": "com.amazon.amazonvideo.livingroom",
                            "page_id": "dthNewHome",
                            "box_type": "iptv",
                            "source_of_stream": "1 | Home.screen_visible.none.none.none.none.none.none.none | none.screen_visible.none.none.none.none.none.none.none | none.click.tile_click.none.1.1.none.none.com.amazon.amazonvideo.livingroom | none.click.app_click.none.1.none.none.none.none | none.click.tile_click.none.1.1.none.com.amazon.amazonvideo.livingroom.com.amazon.amazonvideo.livingroom",
                            "asset_position": "1",
                            "action": "tile_click",
                            "user_session_id": "e62dc075-62bb-4a33-a3c5-f77b99ac1382-1722427823111",
                            "firmware": "fw:1.2.3",
                            "rail_position": "1"
                        },
                        "model": "qurra",
                        "nct": "0",
                        "nq": "-1",
                        "nt": "0",
                        "os": "Android",
                        "ov": "34",
                        "profileId": "",
                        "sId": "40f15638fa7eb4ed",
                        "ts": "1722427823116",
                        "uid": "vuH1osp61U5uH7lRX0"
                    }
                ],
                "id": "994f8281-e035-4cb5-a69e-ec9ae6287ea9",
                "ts": "1722427823500"
            }


        producer.send('bhonesh-test6', message3)
        # print(f'Sent: {message}')

        # Wait for a second before sending the next message
        time.sleep(30)
        # status = False


if __name__ == "__main__":
    try:
        produce_messages()
    except KeyboardInterrupt:
        print("Stopped by user")
    finally:
        # Close the producer connection
        producer.close()