from django.db import models

job_choices = (
    ('j_ch1', '경영 사무'),
    ('j_ch2', '마케팅,광고,홍보'),
    ('j_ch3', 'IT,인터넷'),
    ('j_ch4', '디자인'),
    ('j_ch5', '무역,유통'),
    ('j_ch6', '영업,고객상담'),
    ('j_ch7', '서비스'),
    ('j_ch8', '연구개발,설계'),
    ('j_ch9', '생산,제조'),
    ('j_ch10', '교육'),
    ('j_ch11', '건설'),
    ('j_ch12', '의료'),
    ('j_ch13', '미디어'),
    ('j_ch14', '전문,특수직'),
)


class CV(models.Model):
    job = models.CharField('', max_length=15, choices=job_choices, default='직무 선택')
    letter = models.TextField('')  # 라벨 제거

    def __str__(self):
        return self.letter
