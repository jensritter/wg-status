# wg-cloudstatus

Nagios/Icinga Plugin to check https://status.watchguard.com/

This Status-Page displayes the Content of this json-endpoints :

    https://status.watchguard.com/api/v2/summary.json
    https://status.watchguard.com/api/v2/incidents.json

## Format of https://status.watchguard.com/api/v2/summary.json

    {
        page: {
            id: "9wcfjgptk1hk",
            name: "WatchGuard Technologies",
            url: "https://status.watchguard.com",
            time_zone: "Etc/UTC",
            updated_at: "2024-12-11T13:07:11.485Z"
        },
        components: [
            /* current status */ 
        ],
        incidents: [ 
            /* contains the changes to components */
        ],
        scheduled_maintenances: [ 
            /* contains the changes to components */
        ],
        status: {
            /* collective status */
        }
    }

## component - Schema

(Elements in .components)

    {
        "id": "7sqmnl397kvc",
        "name": "Web UI Login:::EMEA",
        "status": "partial_outage",
        "created_at": "2021-04-15T20:17:58.043Z",
        "updated_at": "2024-12-11T08:40:20.588Z",
        "position": 1,
        "description": null,
        "showcase": false,
        "start_date": "2021-04-14",
        "group_id": "tjcj05gx2pqt",
        "page_id": "9wcfjgptk1hk",
        "group": false,
        "only_show_if_degraded": false
    }

Only "name" and "status" should be relevant for monitoring.

### Regions

The name contains the region - seperated by ":::"

	APAC -- asia-pacific 
	AMER -- america
    EMEA -- Europe, the Middle East and Africa
    GLOB -- Worldwide 
    CORE -- Core ?

## manually checking this with :

    curl -s 'https://status.watchguard.com/api/v2/summary.json' | jq  -r '.components[] | [.status, .name] | join (" ") '  | grep -v "^operational" | grep -v ":::(AMER|APAC)"




