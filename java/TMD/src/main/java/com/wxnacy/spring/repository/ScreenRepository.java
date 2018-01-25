package com.wxnacy.spring.repository;

import java.util.List;

import com.wxnacy.spring.bean.Screen;

public interface ScreenRepository extends BaseRepository<Screen, Long> {
    Screen findByCode(String code);
}
