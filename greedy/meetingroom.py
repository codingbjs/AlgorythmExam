"""
한 회의실이 있다.
이를 사용하고자 하는 N개의 회의들에 대하여 회의실 사용표를 만들려고 한다.
각 회의 idx 에 대해 시작시간과 종료시간이 주워져 있다.
각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라
단, 회의는 한번 시작 하면 중간에 중단할 수 없으며
한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
"""

meetings = [
    {'idx': 1, 'start': 1, 'end': 10}
    , {'idx': 2, 'start': 5, 'end': 6}
    , {'idx': 3, 'start': 13, 'end': 15}
    , {'idx': 4, 'start': 14, 'end': 17}
    , {'idx': 5, 'start': 8, 'end': 14}
    , {'idx': 6, 'start': 3, 'end': 12}
]


def schedule_meeting(_meetings):
    # 종료 시간으로 정렬
    sorted_meetings = sorted(_meetings, key=lambda x: x['end'])

    selected_meetings = []  # 선택된 회의를 저장할 리스트
    end_time = 0  # 현재 회의실의 끝나는 시간 초기화

    for meeting in sorted_meetings:
        if meeting['start'] >= end_time:
            selected_meetings.append(meeting)
            end_time = meeting['end']

    return selected_meetings


def schedule_meeting_1(_meetings):
    res = []
    sort_meetings = sorted(_meetings, key=lambda el: el['end'])

    res.append(sort_meetings[0])

    for e in sort_meetings[1:]:
        if res[-1]['end'] <= e['start']:
            res.append(e)

    return res


print(schedule_meeting(meetings))
print(schedule_meeting_1(meetings))

"""
[{'idx': 2, 'start': 5, 'end': 6}, {'idx': 5, 'start': 8, 'end': 14}, {'idx': 4, 'start': 14, 'end': 17}]
"""
