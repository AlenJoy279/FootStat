package com.example.footstattest.models.jaime;

import java.util.ArrayList;
import java.util.List;

public class Standing {
    private String stage;
    private String type;
    private Object group;
    private List<Table> table = new ArrayList<>();

    public Standing(String stage, String type, Object group, List<Table> Table){
        this.stage = stage;
        this.type = type;
        this.group = group;
        this.table = table;
    }

    // Getters and Setters
    public String getStage() {
        return stage;
    }
    public void setStage(String stage) {
        this.stage = stage;
    }

    public String getType() {
        return type;
    }
    public void setType(String type) {
        this.type = type;
    }

    public Object getGroup() {
        return group;
    }
    public void setGroup(Object group) {
        this.group = group;
    }

    public List<Table> getTable() {
        return table;
    }
    public void setTable(List<Table> table) {
        this.table = table;
    }
}
