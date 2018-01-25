package com.wxnacy.spring.controller;

import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import com.wxnacy.spring.bean.Screen;
import com.wxnacy.spring.repository.ScreenRepository;


@RestController
public class ScreenController {

    @Autowired
    private ScreenRepository screenRepository;

	@GetMapping("/screen")
    public Screen screenByCode(
        @RequestParam(required=true) String code
            ) {
        // List<Screen> items = screenRepository.findByCode(code);
        Screen item = screenRepository.findByCode(code);
        // Screen item = items.get(0);
        System.out.println(item);
        Screen s = screenRepository.getOne(57l);
        System.out.println(s);
        return item;
	}

	@GetMapping("/screen/{id}")
    public Screen screenById(
        @PathVariable Long id
            ) {
        Screen item = screenRepository.findById(id);
        System.out.println(item);
        return item;
	}

}
